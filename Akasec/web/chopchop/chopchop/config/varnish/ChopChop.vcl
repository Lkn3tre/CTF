vcl 4.0;

backend shop-frontend {
    .host = "shop-frontend";
    .port = "80";
}
backend voucher {
    .host = "shop-voucher";
    .port = "6969";
}

sub vcl_pipe {
    if (req.http.upgrade) {
        set bereq.http.upgrade = req.http.upgrade;
	    set bereq.http.connection = req.http.connection;
    }
}
sub vcl_recv {
    if (req.url ~ "^/socket.io/") {
        set req.backend_hint = voucher;
    } else {
        set req.backend_hint = shop-frontend;
    }

    if (req.http.Upgrade ~ "(?i)websocket") {
        set req.backend_hint = voucher;
        return (pipe);
    }
    else {
        set req.backend_hint = shop-frontend;
    }
}