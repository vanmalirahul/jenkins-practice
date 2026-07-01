package com.example;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class HelloServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
                         throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        out.println("<html><body style='text-align:center; font-family:Arial;'>");
        out.println("<h1>Hello from Jenkins + Ansible + Tomcat! 🚀</h1>");
        out.println("<p>Deployed by: Jenkins Pipeline</p>");
        out.println("<p>Server: " + request.getServerName() + "</p>");
        out.println("</body></html>");
    }
}
