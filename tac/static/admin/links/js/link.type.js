var LinkType = (function($) {
    'use_strict';

    var $doc = $( document );

    $.fn.link_type_selector = widgets;

    $doc.ready( function() {
        $( '.form-row.field-link_type select' ).link_type_selector();
    } );

    function widgets() {
        if( this.length > 0 ) {
            return this.each( widget );
        } else {
            return this;
        }
    };

    function widget() {

        var w = this;
        var selectors = [];
        w.$ = $( this );
        w._field_map = {};
        w.$has_detail = $( '.field-has_detail').css({display: 'none'}).find('input');
        w.$options = $('option', w.$).each( prepare );
        w.$fields = $(selectors.join(', '));

        change_link_type();
        w.$.on( 'change', change_link_type );

        function prepare() {
            var $subs;
            var o = this;
            var s = 'field-' + o.value;
            var $e = $('.' + s);
            if(o.value) {
                if($e.length < 1) {
                    $subs = $('div[class*="' + s + '"]');
                    $subs.wrapAll(
                        '<div class="'
                            + 'form-row'
                            + ' field-link_type'
                            + ' language-fields-wrap'
                            + ' ' + s
                            + '" />'
                    );
                    $e = $('.' + s);
                }
                selectors.push('.' + s);
                w._field_map[o.value] = $e;
            }
            if(o.value === 'link_cms_page') {
                w._field_map[o.value].append($('.field-link_cms_plugin'));
            }
        };

        function change_link_type( e ) {
            var value = w.$.val()
            w.$fields.addClass('pseudo-hidden');
            if(value==='has_detail') {
                w.$has_detail.attr('checked', 'checked');
            } else {
                w.$has_detail.removeAttr('checked');
            }
            if(value) {
                w._field_map[value].removeClass('pseudo-hidden');
            }
        };

        return w;
    };
})(django.jQuery);