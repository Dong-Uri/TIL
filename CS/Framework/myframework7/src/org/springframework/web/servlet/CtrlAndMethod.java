package org.springframework.web.servlet;

import java.lang.reflect.Method;

public class CtrlAndMethod {
	private Object target;
	private Method method;

	public CtrlAndMethod(Object target, Method method) {
		this.target = target;
		this.method = method;
	}

	public Object getTarget() {
		return target;
	}
	public void setTarget(Object target) {
		this.target = target;
	}
	public Method getMethod() {
		return method;
	}
	public void setMethod(Method method) {
		this.method = method;
	}
}
