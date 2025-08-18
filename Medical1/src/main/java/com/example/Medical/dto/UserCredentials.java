package com.example.Medical.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class UserCredentials{
    private String id;
    private String name;
    private String password;
    private String email;
    private String phone;
}
