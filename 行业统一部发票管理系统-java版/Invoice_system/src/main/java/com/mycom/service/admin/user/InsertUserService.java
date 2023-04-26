package com.mycom.service.admin.user;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemUserEntity;

import java.util.LinkedHashMap;

public interface InsertUserService extends IService<SystemUserEntity> {
    public LinkedHashMap InsertUser(SystemUserEntity systemUserEntity);
}
