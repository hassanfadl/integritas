odoo.define('mx_integritas_cp_ventauto.website_codigo', function (require) {
    'use strict';
    

    var core = require('web.core');
    var publicWidget = require('web.public.widget');
    var concurrency = require('web.concurrency');
    var dp = new concurrency.DropPrevious();

    var _t = core._t;

  
    
    publicWidget.registry.website_codigo = publicWidget.Widget.extend({
        
        selector: '.div_zip',
        events: {
            'keyup input[name="zip"]': '_onKeyUpCodigo'
        },
        init: function () {
            
            console.log('Integritas MX Start Ventauto');
            this._super.apply(this, arguments);
            this._popoverRPC = null;

        },
        start: function() {
            
            console.log('start');
            var select = $("select[name='mx_integritas_colonia']")
            var input = $("input[name='l10n_mx_edi_colony']")
            if(select.val()==""|| select.val()==null){
                select.css("display","none")
                input.css("display","block")
            }else{
                select.css("display","block")
                input.css("display","none")
            }
            $(".col-form-label").append("*")
            
            
            // will print "div.oe_petstore_greetings" in the console
        },
        /**
         * @private
         * @param {Event} ev
         */
        _onKeyUpCodigo: function (ev) {
            //var $radio = $(ev.currentTarget).find('input[name="zip"]')
            var $codigo = $(ev.currentTarget).val()
            if($codigo.length==5){
                var select = $("select[name='mx_integritas_colonia']")
                var input = $("input[name='l10n_mx_edi_colony']")
                
                $.ajax({
                    url: "https://api-sepomex.hckdrk.mx/query/info_cp/"+$codigo+"?token=a94b5161-ee6f-4a08-8c2d-af86caebee62",
                    cache: false,
                    success: function(html){
                        select.val("").html("")
                        $("#mx_integritas_colonia").html("")
                        for(let index in html){
                            html[index].asentamiento;
                            var asentamiento = html[index].response.asentamiento;
                            $("#mx_integritas_colonia").append(`<option value="`+asentamiento+`">`+asentamiento+`</option>`)
                        }
                        $("input[name='l10n_mx_edi_colony']").val($("#mx_integritas_colonia").val())
                        var response = html[0].response
                        
                        $("input[name='city']").val(response.municipio)
                        $("select[name ='country_id'] > option").each(function() {
                        
                            if(this.text.toUpperCase() == "México".toUpperCase()){
                                var country = this.value;
                                $("select[name ='country_id']").on('change', function(){
                                    $("select[name ='country_id']").val(country)

                                });
                                var time = 300;
                                var iCount = 0;
                                $("select[name ='state_id'] > option").each(function() { iCount++;})
                                if(iCount<=2){
                                    $("select[name ='country_id']").trigger('change')
                                    time = 1300;
                                }
                    
                                setTimeout(function(){
                                    var _exist__ = 0;
                                   
                                    $("select[name ='state_id'] > option").each(function() {
                                        if(this.text.toUpperCase() == response.estado.toUpperCase()){
                                            $("select[name ='state_id']").val(this.value)
                                            _exist__ = 1;
                                        }
                                    });
                                    if(_exist__ == 0){
                                        $("select[name ='state_id'] > option").each(function() {
                                            if(response.estado.toUpperCase().indexOf(this.text.toUpperCase())!=-1){
                                                $("select[name ='state_id']").val(this.value)
                                                _exist__ = 1;
                                            }
                                            
                                        });
                                    }
                                    
                                },time)
                            }
                        });
                        if(select.val()==""|| select.val()==null){
                            select.css("display","none")
                            input.css("display","block")
                        }else{
                            select.css("display","block")
                            input.css("display","none")
                        }
                        
                    },error: function (request, status, error) {
                        select.val("").html("")
                        $("select[name ='state_id']").val("")
                        $("select[name ='country_id'] > option").each(function() {
                            if(this.text.toUpperCase() == "México".toUpperCase()){
                                var country = this.value;
                                $("select[name ='country_id']").on('change', function(){
                                    $("select[name ='country_id']").val(country)

                                });
                            }
                        });
                        $("input[name='city']").val("")
                        if(select.val()==""|| select.val()==null){
                            select.css("display","none")
                            input.css("display","block")
                        }else{
                            select.css("display","block")
                            input.css("display","none")
                        }
                    }
                });
                
            }else{
                $("input[name='zip']").val($codigo.substring(0,5))
            }
 
        },
        
    });
    
});