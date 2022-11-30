package org.springframework.web.servlet.handler;
// 사용자 요청에 해당하는 컨트롤 클래스 정보 관리..

import java.util.HashMap;
import java.util.Map;

import org.springframework.web.servlet.HandlerMapping;
import org.springframework.web.servlet.mvc.Controller;

import com.ssafy.myframework.controller.BoardController;
import com.ssafy.myframework.controller.UserController;

public class PathSettingHandlerMapping implements HandlerMapping {
	// 특정 URI와 컨트롤 클래스 정보를 담기 위한 맵 객체 선언
	private Map<String, Controller> mappings = new HashMap<>();
	
	public PathSettingHandlerMapping() {
		mappings.put("/board", new BoardController());
		mappings.put("/user", new UserController());
	}
	
	public Controller getHandler(String uri) {
		return mappings.get(uri);
	}
}













