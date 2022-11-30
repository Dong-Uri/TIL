package org.springframework.web.servlet.mvc;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public interface Controller {
	public String service(
			HttpServletRequest request, HttpServletResponse response) 
					throws Exception;
}