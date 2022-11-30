package org.springframework.web.servlet;
// 사용자 요청에 해당하는 컨트롤 클래스 정보 관리..

public interface HandlerMapping {
	public CtrlAndMethod getHandler(String uri);
}