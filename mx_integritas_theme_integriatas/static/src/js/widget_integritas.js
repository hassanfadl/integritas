odoo.define('mx_integritas_theme_integriatas.website_widget', function (require) {
    'use strict';
    

    var core = require('web.core');
    var publicWidget = require('web.public.widget');
    var concurrency = require('web.concurrency');
    var dp = new concurrency.DropPrevious();

    var _t = core._t;
    
    
    publicWidget.registry.mxIntegritasThemeIntegriatas = publicWidget.Widget.extend({
        
        selector: '#wrapwrap',
        events: {
            'click #btn-whatsapp-integritas': '_botonWhatsApp',
            'click #btn-integritas-ws-submit': '_botonWhatsApp_submit',
            'click #close-ws-integritas': '_botonWhatsApp_close',
            'click #btn-up-page': '_boton_up_page',




        },
        init: function () {
            this._super.apply(this, arguments);
            this._popoverRPC = null;
        },
        start: function() {
            console.log("Start Integritas")
            
        },
         _botonWhatsApp: function (ev) {
            $("#whats-integritas").removeClass("invisible-ws")  
            dp.add(this._rpc({route: '/whatsapp/get_text',})).then(this._HandleGetText.bind(this));          
        },
        _boton_up_page:function(ev){
            $("html, body").animate({ scrollTop: 0 }, "slow");
        },_botonWhatsApp_submit: function (ev) {

            var name = $("input[name='wsintegritasname']").val();
            var email = $("input[name='wsintegritasemail']").val();
            var phone = $("input[name='wsintegritasphone']").val();
            if(name!=""&& email!=""&& phone!=""&& email.indexOf("@")!=-1 && email.indexOf(".")!=-1 && phone.length >=8 && phone.length <= 10){
                dp.add(this._rpc({
                route: '/whatsapp/crear_oportunidad',
                params: {
                    name: name,
                    email: email,
                    phone: phone,
                },
                })).then(this._handleRedirectUrl.bind(this));


            }else{
                $("#error_whatsapp").removeClass('invisible')
            }           
        },
        _botonWhatsApp_close: function (ev) {
            $("#whats-integritas").addClass("invisible-ws")         
        },
        

        _handleRedirectUrl: function (result) {
            //window.location.href="https://api.whatsapp.com/message/ODJWOG3OBNQJD1"   
            window.open('https://api.whatsapp.com/message/ODJWOG3OBNQJD1', '_blank');         
        },
        _HandleGetText: function (result) {
            //window.location.href="https://api.whatsapp.com/message/ODJWOG3OBNQJD1"   
           setTimeout(function(){
                $("#text_whatsapp").html(result)   
            }, 1500);
               
        },


        
        
    });
});