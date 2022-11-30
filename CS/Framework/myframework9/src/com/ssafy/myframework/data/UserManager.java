package com.ssafy.myframework.data;

import java.util.ArrayList;
import java.util.List;

import com.ssafy.myframework.model.User;

public class UserManager {
    private static List<User> users = new ArrayList<>();
    static {
        for (int i = 0; i < 10; i++) {
            users.add(new User("ssafy" + i, "싸피" + i, "ssafy" + i + "@ssafy.com", "000" + i));
        }
    }
    
    private static UserManager instance = new UserManager();
    
    public static UserManager getInstance() {
        return instance;
    }
    
    public List<User> selectUser() {
        List<User> users = new ArrayList<>();
        users.addAll(UserManager.users);
        return users;
    }

    public void insertUser(User user) {
        users.add(user);
    }
}
