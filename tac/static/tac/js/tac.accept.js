var TACAccept = ( function( $ ) {
    'use strict';

    var selector = '.tac-popup';
    var button_selector = '.tac-popup-button';

    $.fn.tac_accept = widgets;

    init();

    return {
        init: init
    };

    function init() {
        $( selector ).tac_accept();
    };

    function widgets() {
        return this.each( widget );
    };

    function widget() {
        var w = this;
        w.$ = $( this );
        w.$button = $( button_selector, w.$ );
        w.$button[0]._url = w.$button.attr( 'href' );
        w.$button[0]._apiurl = w.$button.data( 'apiurl' );
        w.$button[0]._parent = w;

        w.$button.on( 'click', accept );
    };

    function accept( e ) {
        try { e.preventDefault(); } catch( e ) {}
        var b = this;
        $.ajax( {
            method: 'get',
            url: b._apiurl,
        } ).done( function( data ) {
            if( data.message === 'ok' ) {
                b._parent.$.remove();
            } else {
                window.location.href = b._url;
            }
        });
    }

} )( jQuery );