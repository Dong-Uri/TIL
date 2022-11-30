package com.ssafy.myframework.model;

public class Board {
	private int no;
	private String title;
	private String writer;
	private int viewCnt;
    public Board() {
    }
    public Board(String title, String writer, int viewCnt) {
        this.title = title;
        this.writer = writer;
        this.viewCnt = viewCnt;
    }
    public int getNo() {
        return no;
    }
    public void setNo(int no) {
        this.no = no;
    }
    public String getTitle() {
        return title;
    }
    public void setTitle(String title) {
        this.title = title;
    }
    public String getWriter() {
        return writer;
    }
    public void setWriter(String writer) {
        this.writer = writer;
    }
    public int getViewCnt() {
        return viewCnt;
    }
    public void setViewCnt(int viewCnt) {
        this.viewCnt = viewCnt;
    }
    @Override
    public String toString() {
        return "Board [no=" + no + ", title=" + title + ", writer=" + writer + ", viewCnt=" + viewCnt + "]";
    }
}
