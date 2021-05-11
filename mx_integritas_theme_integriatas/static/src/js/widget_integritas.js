/*odoo.define('mx_integritas_theme_integriatas.website_widget', function (require) {
    'use strict';
    

    var core = require('web.core');
    var publicWidget = require('web.public.widget');
    var concurrency = require('web.concurrency');
    var dp = new concurrency.DropPrevious();

    var _t = core._t;
    
    
    publicWidget.registry.mxIntegritasThemeIntegriatas = publicWidget.Widget.extend({
        
        selector: 'a',
        events: {
            'click .flotante': '_botonWhatsApp',
          
            
        },
        init: function () {
            
            
            this._super.apply(this, arguments);
            this._popoverRPC = null;
            
            
            

        },
        start: function() {
            alert("Starttt")
        },

    
         _botonWhatsApp: function (ev) {
            alert("Whats")
            
            dp.add(this._rpc({
                route: '/cotizador_auto/marca',
                params: {
                    anio_id: anio,
                    llave: llave,
                    edi: edi,
                },
            })).then(this._handleMarca.bind(this));
            
        },
        

        _handleMarca: function (result) {
            console.log(result)
            
        },


        
        
    });
});*/