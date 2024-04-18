
invoice_html_content = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <title>{% if pdf_title %}{{ pdf_title }}{% else %}PDF{% endif %}</title>
        <style type="text/css">
            body {
                font-weight: 200;
                font-size: 14px;
            }
            .header {
                font-size: 20px;
                font-weight: 100;
                text-align: center;
                color: #007cae;
            }
            .title {
                font-size: 22px;
                font-weight: 100;
                /* text-align: right;*/
                padding: 10px 20px 0px 20px;
            }
            .title span {
                color: #007cae;
            }
            .details {
                padding: 10px 20px 0px 20px;
                text-align: left !important;
                /*margin-left: 40%;*/
            }
            .hrItem {
                border: none;
                height: 1px;
                /* Set the hr color */
                color: #333; /* old IE */
                background-color: #fff; /* Modern Browsers */
            }
        </style>
    </head>
    <body>
        <div class='wrapper'>
            <div class='header'>
                <p class='title'>Invoice #{{ invoice_number}}</p>
            </div>
        <div>
        <div class='details'>
            Bill to: {{ customer_name }}<br/>
            Amount: {{ amount }} <br/>
            Date: {{ date }}
            <hr class='hrItem' />
        </div>
    </div>
    </body>
</html>
"""
