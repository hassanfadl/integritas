odoo.define("mx_integriats_mass_mailing.popup", function(require){
  var InheritedWidget = require('mass_mailing.website_integration'); 
  console.log(InheritedWidget)
  InheritedWidget.Widget.include({
    /*init: function(parent, options) {
        this.events["click .js_subscribe_btn"] = "_onSubscribeClick";
        this._super(parent, options);
    },*/
    
    _onSubscribeClick_dos: async function () {
        alert("demo")
    },
  });
})