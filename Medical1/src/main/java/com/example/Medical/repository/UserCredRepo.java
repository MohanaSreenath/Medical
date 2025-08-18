package com.example.Medical.repository;

import com.example.Medical.entity.UserCredEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserCredRepo extends JpaRepository<UserCredEntity, Long> {
    List<UserCredEntity> findByEmail(String email);
    // You can add custom queries here if needed
}
