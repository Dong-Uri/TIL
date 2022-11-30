package org.springframework.web.util;

import java.lang.reflect.Method;

import javax.servlet.http.HttpServletRequest;

public class WebUtil {
	
	@SuppressWarnings("unchecked")
	public static <T> T getParamToVO(HttpServletRequest req, Class<T> clz) throws Exception {
		Object obj = clz.getDeclaredConstructor().newInstance();
		Method[] mArr = clz.getDeclaredMethods();
		
		for (Method m : mArr) {
			String mName = m.getName();
			if (!mName.startsWith("set")) continue;
			
			mName = mName.substring("set".length());
			mName = Character.toLowerCase(mName.charAt(0)) + mName.substring(1);
			
			String[] pValue = req.getParameterValues(mName); 
			if (pValue == null) continue;
			
			String pTypeName = m.getParameterTypes()[0].getName();
			switch (pTypeName) {
			case "int":
				m.invoke(obj, Integer.parseInt(pValue[0]));
				break;
			case "String":
				m.invoke(obj, pValue[0]);
				break;
			default:
				m.invoke(obj, pValue[0]);
				break;
			}
		}
		return (T)obj;
	}
}





