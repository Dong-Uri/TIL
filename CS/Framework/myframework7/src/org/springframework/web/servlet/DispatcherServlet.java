package org.springframework.web.servlet;

import java.io.IOException;
import java.lang.reflect.Method;
import java.util.Map;
import java.util.Set;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.handler.PathSettingHandlerMapping;
import org.springframework.web.servlet.view.UrlBasedViewResolver;

public class DispatcherServlet extends HttpServlet {

	private static final long serialVersionUID = -8007253319839750377L;
	
	private HandlerMapping mapping;
	public void init(ServletConfig config) throws ServletException {
		try {
			mapping = new PathSettingHandlerMapping(
					config.getInitParameter("controllers")
			);
		} catch (Exception e) {
			throw new ServletException(e);
		}
	}
	
	@Override
	public void service(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		try {
			// 웹컨텍스트(웹어플리케이션, 웹프로젝트) 경로
			String contextPath = request.getContextPath();
			
			// 사용자 요청 경로 
			String requestUri = request.getRequestURI();
			
			requestUri = requestUri.substring(contextPath.length());
			
			// uri에 해당하는 컨트롤러 반환
			CtrlAndMethod cam = mapping.getHandler(requestUri);
			if (cam == null) {
				throw new ServletException("요청하신 URL이 존재하지 않습니다.");
			}
			
			// 컨트롤러 작업 .. 실행
			Object target = cam.getTarget();
			Method m = cam.getMethod();

			ModelAndView mav = (ModelAndView)m.invoke(target, request, response);
			String view = mav.getViewName();
			
			// view가 forward, redirect 해야 할지 구분..
			if (view.startsWith(UrlBasedViewResolver.REDIRECT_URL_PREFIX)) {
				response.sendRedirect(view.substring(UrlBasedViewResolver.REDIRECT_URL_PREFIX.length()));
			}
			else {
				// 화면에서 사용할 데이터 공유 : mav객체에 들어있는 model 객체를 꺼내서 공유시키기
				Map<String, Object> model = mav.getModel();
				// 맵의 모든 키를 Set 객체에 담아서 반환
				Set<String> keys = model.keySet();
				for (String key : keys) {
					request.setAttribute(key, model.get(key));
				}
				
				// 페이지 이동하기
				RequestDispatcher rd = request.getRequestDispatcher(view);
				rd.forward(request, response);
			}
			
		} catch (Exception e) {
			throw new ServletException(e);
		}
	}
}









