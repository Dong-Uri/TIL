package org.springframework.web.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.ssafy.myframework.controller.BoardController;
import com.ssafy.myframework.controller.UserController;

public class DispatcherServlet extends HttpServlet {

	private static final long serialVersionUID = 8800397388105277770L;

	@Override
	public void service(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		try {
			if (request.getMethod().equals("POST")) {
				request.setCharacterEncoding("UTF-8");
			}			
			
			// 웹컨텍스트(웹어플리케이션, 웹프로젝트) 경로
			String contextPath = request.getContextPath();
			System.out.println("contextPath : " + contextPath);
			
			// 사용자 요청 경로 
			String requestUri = request.getRequestURI();
			System.out.println("uri : " + requestUri);
			
			requestUri = requestUri.substring(contextPath.length());
			System.out.println("uri : " + requestUri);
			
			switch (requestUri) {
			case "/board":
				BoardController board = new BoardController();
				board.service(request, response);
				break;	
			case "/user":
				UserController user = new UserController();
				user.service(request, response);
				break;	
			}
			
		} catch (Exception e) {
			throw new ServletException(e);
		}
	}
}









