odoo.define('mx_integritas_popup_marketing.popup', function (require) {
  'use strict';
  

  var core = require('web.core');
  var publicWidget = require('web.public.widget');
  var concurrency = require('web.concurrency');
  var massMailing = require("mass_mailing.website_integration");
  var dp = new concurrency.DropPrevious();
  const {ReCaptcha} = require('google_recaptcha.ReCaptchaV3');
  var _t = core._t;
  
  publicWidget.registry.subscribe = publicWidget.Widget.extend({
    selector: ".js_subscribe",
    disabledInEditableMode: false,
    read_events: {
        'click .js_subscribe_btn': '_onSubscribeClick',
    },/**
    * @constructor
    */
    start:  function () {
      var self = this;
      var def = this._super.apply(this, arguments);
      this._super(...arguments);
      this._recaptcha = new ReCaptcha();
      this.$popup = this.$target.closest('.o_newsletter_modal');
      if (this.$popup.length) {
          // No need to check whether the user subscribed or not if the input
          // is in a popup as the popup won't open if he did subscribe.
          return def;
      }
    },
    _onSubscribeClick: async function () {
      var self = this;
      var $email = this.$(".js_subscribe_email:visible");
      var $name = this.$(".js_subscribe_name:visible");
      console.log($email.val())
      if ($email.length && !$email.val().match(/.+@.+/) ) {
          this.$target.addClass('o_has_error').find('.form-control').addClass('is-invalid');
          return false;
      }
      if($name.val().length < 3){
        $name.addClass('o_has_error is-invalid').find('.form-control').addClass('is-invalid');
        return false;
      }
      this.$target.removeClass('o_has_error').find('.form-control').removeClass('is-invalid');
      const tokenObj = await this._recaptcha.getToken('website_form');
      if (tokenObj.error) {
          self.displayNotification({
              type: 'danger',
              title: _t("Error"),
              message: tokenObj.error,
              sticky: true,
          });
          return false;
      }
      
      this._rpc({
          route: '/website_mass_mailing/subscribe/replace',
          params: {
              'list_id': this.$target.data('list-id'),
              'email': $email.length ? $email.val() : false,
              'name' : $name.val().toLowerCase(),
              recaptcha_token_response: tokenObj.token,
          },
      }).then(function (result) {
          let toastType = result.toast_type;
          if (toastType === 'success') {
              self.$(".js_subscribe_btn").addClass('d-none');
              self.$(".js_subscribed_btn").removeClass('d-none');
              self.$('input.js_subscribe_email').prop('disabled', !!result);
              if (self.$popup.length) {
                  self.$popup.modal('hide');
              }
          }
          self.displayNotification({
              type: toastType,
              title: toastType === 'success' ? _t('Success') : _t('Error'),
              message: result.toast_content,
              sticky: true,
          });
      });
    },
  });
});