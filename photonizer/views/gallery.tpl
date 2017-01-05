<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>{{path}}</title>
        <style>
            html, body {
                background-color: #000000;
                margin: 0;
                padding: 0;
            }
            body {
                padding: 10px;
            }
            #photos {
                /* Prevent vertical gaps */
                line-height: 0;

                -webkit-column-count: 5;
                -webkit-column-gap:   10px;
                -moz-column-count:    5; -moz-column-gap:      10px;
                column-count:         5;
                column-gap:           10px;
            }

            #photos img {
                width: 100% !important;
                height: auto !important;
            }
            #photos a {
                margin-bottom: 10px;
                display: block;
                position: relative;
            }
            #photos span.text-content {
                opacity: 0;
                position: absolute;
                bottom: 0;
                left: 0;
                    right: 5px;
                        padding: 10px;
                width: 100%;
                background: #cccccc;
                color: #ffffff;
            }
            #photos a:hover span.text-content {
                opacity: 1;
                padding: 5px;
            }
            span.text-content span {
                display: table-cell;
                text-align: center;
                vertical-align: middle;
            }

@media (max-width: 1200px) {
  #photos {
  -moz-column-count:    4;
  -webkit-column-count: 4;
  column-count:         4;
  }
}
@media (max-width: 1000px) {
  #photos {
  -moz-column-count:    3;
  -webkit-column-count: 3;
  column-count:         3;
  }
}
@media (max-width: 800px) {
  #photos {
  -moz-column-count:    2;
  -webkit-column-count: 2;
  column-count:         2;
  }
}
@media (max-width: 400px) {
  #photos {
  -moz-column-count:    1;
  -webkit-column-count: 1;
  column-count:         1;
  }
}
        </style>
    </head>

    <body>
        % if directories:
        <ul>
            % for directory in directories:
            <li><a href="/{{directory}}">{{directory}}</a></li>
            % end
        </ul>
        % end
        <section id="photos">
            % for file in files:
            <a href="/{{path}}/{{file}}">
                <img src="/thumbs/{{path}}/{{file}}" />
                <span class="text-content"><span>{{file}}</span></span>
            </a>
            % end
        </section>
    </body>
</html>
