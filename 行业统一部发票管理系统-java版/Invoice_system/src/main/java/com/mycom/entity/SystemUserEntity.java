package com.mycom.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("system_user")
public class SystemUserEntity {
    @TableId(value = "id",type = IdType.AUTO)
    private Integer id;
    private String user_login_name;
    private String user_name;
    private String password;
    private Integer company_id;
    private Integer department_id;
}
