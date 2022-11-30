package com.ssafy.myframework.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;
import org.springframework.web.util.WebUtil;

import com.ssafy.myframework.data.BoardManager;
import com.ssafy.myframework.model.Board;

public class BoardController implements Controller {

    private BoardManager manager;
    
    public BoardController() {
        manager = BoardManager.getInstance();
	}
	
	public ModelAndView service(HttpServletRequest request, HttpServletResponse response)
			throws Exception {
		
		ModelAndView mav = null;
		
		String act = request.getParameter("act");
		if (act == null) act = "list";
		switch (act) {
		case "list":
			mav = list(request, response);
			break;
		case "write-form":
			mav = writeForm(request, response);
			break;
		case "write":
			mav = write(request, response);
			break;
		}
		return mav;
	}

	public ModelAndView writeForm(HttpServletRequest request, HttpServletResponse response)
            throws Exception {
		return new ModelAndView("/board/write-form.jsp");
    }

    public ModelAndView list(HttpServletRequest request, HttpServletResponse response) throws Exception {
    	ModelAndView mav = new ModelAndView("/board/list.jsp");
    	mav.addObject("list", manager.selectBoard());
        return mav;
    }

    public ModelAndView write(HttpServletRequest request, HttpServletResponse response) throws Exception {
        manager.insertBoard(WebUtil.getParamToVO(request, Board.class));
        return new ModelAndView("redirect:board?act=list");
    }
}
