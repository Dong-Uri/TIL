package org.springframework.web.servlet.handler;
// 사용자 요청에 해당하는 컨트롤 클래스 정보 관리..

import java.lang.reflect.InvocationTargetException;
import java.util.HashMap;
import java.util.Map;

import org.springframework.web.servlet.HandlerMapping;
import org.springframework.web.servlet.mvc.Controller;

import com.ssafy.myframework.controller.BoardController;
import com.ssafy.myframework.controller.UserController;

public class PathSettingHandlerMapping implements HandlerMapping {
	// 특정 URI와 컨트롤 클래스 정보를 담기 위한 맵 객체 선언
	private Map<String, Controller> mappings = new HashMap<>();

	public PathSettingHandlerMapping(String controllers) throws InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException, ClassNotFoundException {
//		/board=com.ssafy.myframework.controller.BoardController;
//		/user=com.ssafy.myframework.controller.UserController

		String[] ctrls = controllers.split(";");

		for (String ctrl : ctrls) {
			String[] info = ctrl.trim().split("=");
			mappings.put(info[0], (Controller) Class.forName(info[1]).getDeclaredConstructor().newInstance());
		}
	}

	public Controller getHandler(String uri) {
		return mappings.get(uri);
	}
}
