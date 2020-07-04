function myFunction() {
    var x = document.createElement("INPUT");
    x.setAttribute("type", "file");
    document.body.appendChild(x);
  }

(function ($) {

    skel.init({
        reset: 'full',
        breakpoints: {
         // #Edit  global: { href: 'css/style.css', containers: 1400, grid: { gutters: ['2em', 0] } },
            xlarge: { media: '(max-width: 1680px)', href: 'css/style-xlarge.css', containers: 1200 },

        },
        plugins: {
            layers: {

                // Config.
                config: {
                    transformTest: function () { return skel.vars.isMobile; }
                },

                // Navigation Button.
                navButton: {
                    breakpoints: 'medium',
                    height: '4em',
                    html: '<span class="toggle" data-action="toggleLayer" data-args="navPanel"></span>',
                    position: 'top-left',
                    side: 'top',
                    width: '50'
                },

                // Navigation Panel.
                navPanel: {
                    animation: 'overlayX',
                    breakpoints: 'medium',
                    clickToHide: true,
                    height: '100%',
                    hidden: true,
                    html: '<div data-action="navList" data-args="nav"></div>',
                    orientation: 'vertical',
                    position: 'top-left',
                    side: 'left',
                    width: 250
                }

            }
        }
    });
})


