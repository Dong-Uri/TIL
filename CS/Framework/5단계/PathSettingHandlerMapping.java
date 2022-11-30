package org.springframework.web.servlet.handler;

import java.lang.reflect.InvocationTargetException;
import java.util.HashMap;
import java.util.Map;

import org.springframework.web.servlet.HandlerMapping;
import org.springframework.web.servlet.mvc.Controller;

public class PathSettingHandlerMapping implements HandlerMapping {
	// 특정 URI와 컨트롤 클래스 정보를 담기 위한 맵 객체 선언
	private Map<String, Controller> mappings = new HashMap<>();
	
	public PathSettingHandlerMapping(String controllers) throws InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException, ClassNotFoundException {
		// ctrlNames 의 문자열을 ";" 으로 split 한다.
		String[] ctrls = controllers.split(";");
		// split 된 문자열을 반복을 돌면서 "="으로 2차 split 한다.
		// 주의 : "="으로 split 할 대상 문자을의 양쪽 공백을 제거한다(trim())
		for (String ctrl : ctrls) {
			String[] info = ctrl.trim().split("=");
			// "="으로 split 된 문자열의 앞부분은 맵의 키에 넣고
			// 뒷부분은 리플렉션을 이용해서 객체 생성 한 후 값에 넣는다.(Controller 형변환 후)
			mappings.put(
					info[0], 
					(Controller)(Class.forName(info[1]).getDeclaredConstructor().newInstance())
			);
		}
	}
	
	public Controller getHandler(String uri) {
		return mappings.get(uri);
	}
}