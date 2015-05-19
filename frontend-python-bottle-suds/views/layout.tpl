<!DOCTYPE html>
<html>
<head>
    <title>{{title if defined('title') else "ITEC833"}}</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <script src="/static/jquery-1.11.3.min.js"></script>
</head>
<body>

<ul id="nav">
    <li><a href="/">Home</a></li>
</ul>

% if defined('error') and error:
    <div class="error">{{error}}  </div>
% end

    {{!base}}
</body>
</html>