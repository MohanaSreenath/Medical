package com.example.Medical.service;

import com.example.Medical.entity.UserCredEntity;
import com.example.Medical.repository.UserCredRepo;
import com.example.Medical.repository.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.Medical.dto.User;
import com.example.Medical.entity.UserEntity;

import java.util.ArrayList;
import java.util.List;

@Service
public class UserService {
    @Autowired
    private UserRepo userRepo;

    @Autowired
    private UserCredRepo userCredRepo;

    public void register(User user) {
        UserEntity userEntity = new UserEntity();
        userEntity.setName(user.getName());
        userEntity.setPassword(user.getPassword());
        userEntity.setEmail(user.getEmail());
        userEntity.setPhone(user.getPhone());
        userEntity.setAge(user.getAge());
        userEntity.setGender(user.getGender());
        userEntity.setWeight(user.getWeight());
        userEntity.setHeight(user.getHeight());

        try {
            SaveCredentials(user);
        } catch (Exception e) {
            System.out.println("Error in the Save Credentials method");
        }

        userRepo.save(userEntity);
    }

    public List<User> displayUsers() {
        List<UserEntity> userEntities = userRepo.findAll();
        List<User> users = new ArrayList<>();

        for (UserEntity entity : userEntities) {
            User user = new User();
            user.setName(entity.getName());
            user.setEmail(entity.getEmail());
            user.setPassword(entity.getPassword());
            users.add(user);
        }

        return users;
    }
    public void SaveCredentials(User user) {
        String password = user.getPassword();
        String email = user.getEmail();
        String UserName = user.getName();
        String phone = user.getPhone();
        UserCredEntity userCredEntity = new UserCredEntity();
        userCredEntity.setPassword(password);
        userCredEntity.setEmail(email);
        userCredEntity.setName(UserName);
        userCredEntity.setPhone(phone);

        userCredRepo.save(userCredEntity);
    }

    public void loginCheck(String email, String password) {
        UserEntity userEntity = new UserEntity();
        userCredRepo.findByEmail(email);

    }

}

