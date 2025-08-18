package com.example.Medical.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "MedicalUsers1")
public class UserEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // Use Long for auto-increment
    private String name;
    private String password;
    private String email;
    private String phone;
    private String age;
    private String gender;
    private String weight;
    private String height;
}
