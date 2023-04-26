package com.mycom.service.admin.user;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemUserEntity;

import java.util.LinkedHashMap;

public interface OneUserService extends IService<SystemUserEntity> {
    public LinkedHashMap OneUser(Integer userId);
}
