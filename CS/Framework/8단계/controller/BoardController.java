package com.ssafy.myframework.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.ssafy.myframework.data.BoardManager;
import com.ssafy.myframework.model.Board;

public class BoardController {

    private BoardManager manager;
    
    public BoardController() {
        manager = BoardManager.getInstance();
	}
	
    @RequestMapping("/board/write-form")
	public ModelAndView writeForm() {
		return new ModelAndView("/board/write-form.jsp");
    }

    @RequestMapping("/board/list")
    public ModelAndView list() {
    	ModelAndView mav = new ModelAndView("/board/list.jsp");
    	mav.addObject("list", manager.selectBoard());
        return mav;
    }

    @RequestMapping("/board/write")
    public ModelAndView write(Board board) {
        manager.insertBoard(board);
        return new ModelAndView("redirect:list");
    }
}
