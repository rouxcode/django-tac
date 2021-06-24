var TACAccept = (function () {
    'use strict';

    var popups;

    var selector = '.tac-popup';
    var button_selector = '.tac-popup-button';

    dom_ready(init);

    return { init: init };

    function init() {
        popups = document.querySelectorAll(selector);
        if (popups.length > 0) {
            popups.forEach(init_popup)
        }
    };

    function init_popup(widget) {
        widget._b = widget.querySelector(':scope ' + button_selector);
        widget._b._api = widget._b.dataset.api;
        widget._b._widget = widget;

        // add ajax/fetch request if available
        if ('fetch' in window) {
            widget._b.addEventListener('click', accept);
        }
    };

    function accept(e) {
        e.preventDefault();
        var b = this;
        var w = this._widget;
        fetch(this._api).then(response => {
            if (response.status === 200) {
                return response.json()
            } else {
                document.location = b.href;
            }
        }).then(data => {
            w.remove();
        }).catch(error => {
            document.location = b.href;
        });
    };

    function dom_ready(callback) {
        if (document.readyState != 'loading') {
            callback();
        } else {
            document.addEventListener('DOMContentLoaded', callback);
        }
    };
})();