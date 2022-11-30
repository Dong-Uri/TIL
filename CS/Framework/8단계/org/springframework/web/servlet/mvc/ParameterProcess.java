package org.springframework.web.servlet.mvc;

import java.lang.reflect.Method;
import java.lang.reflect.Parameter;

import javax.servlet.http.HttpServletRequest;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.util.WebUtil;

public class ParameterProcess {

	public static Object[] process(Method m, HttpServletRequest request) throws Exception {
		Parameter[] pArr = m.getParameters();
		Object[] rArr = new Object[pArr.length];
		int index = 0;
		for (Parameter param : pArr) {
			Class<?> tClz = param.getType();
			String tName = tClz.getSimpleName();
			String name = param.getName();
			switch (tName) {
			case "String":
				rArr[index++] = request.getParameter(name);
				break;
			case "int":
				rArr[index++] = Integer.parseInt(request.getParameter(name));
				break;
			case "HttpServletRequest":
				rArr[index++] = request;
				break;
			case "ModelAndView":
				rArr[index++] = new ModelAndView();
				break;
			default:
				rArr[index++] = WebUtil.getParamToVO(request, tClz);
			}			
		}
		return rArr;
	}

}









