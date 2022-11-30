package org.springframework.web.servlet.handler;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.HashMap;
import java.util.Map;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.CtrlAndMethod;
import org.springframework.web.servlet.HandlerMapping;

public class PathSettingHandlerMapping implements HandlerMapping {
	// 특정 URI와 컨트롤 클래스 정보를 담기 위한 맵 객체 선언
	private Map<String, CtrlAndMethod> mappings = new HashMap<>();
	
	public PathSettingHandlerMapping(String controllers) throws InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException, NoSuchMethodException, SecurityException, ClassNotFoundException {
		// ctrlNames 의 문자열을 ";" 으로 split 한다.
		String[] ctrls = controllers.split(";");
		
		for (String ctrl : ctrls) {
			
			Class<?> clz = Class.forName(ctrl.trim());
			Object target = clz.getDeclaredConstructor().newInstance();
			Method[] methods = clz.getDeclaredMethods();
			
			for (Method m : methods) {
				RequestMapping rm = m.getAnnotation(RequestMapping.class);
				if (rm == null) continue;
				
				mappings.put(rm.value(), new CtrlAndMethod(target, m));
			}
			
		}
	}
	
	public CtrlAndMethod getHandler(String uri) {
		return mappings.get(uri);
	}
}