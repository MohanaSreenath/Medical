package com.example.Medical.repository;

import com.example.Medical.entity.UserEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface UserRepo extends JpaRepository<UserEntity, Long> {

    // Custom query to find a user by email
    Optional<UserEntity> findByEmail(String email);

    // Check if a user exists with given email
    boolean existsByEmail(String email);

    // You can also search by username or other fields
    Optional<UserEntity> findByName(String username);
}
