package org.springframework.web.servlet;
// 사용자 요청에 해당하는 컨트롤 클래스 정보 관리..

import org.springframework.web.servlet.mvc.Controller;

public interface HandlerMapping {
	public Controller getHandler(String uri);
}













