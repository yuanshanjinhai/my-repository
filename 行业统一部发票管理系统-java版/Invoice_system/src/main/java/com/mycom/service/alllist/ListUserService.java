package com.mycom.service.alllist;

import com.baomidou.mybatisplus.extension.service.IService;
import com.mycom.entity.SystemUserEntity;

import java.util.LinkedHashMap;

public interface ListUserService extends IService<SystemUserEntity> {
    public LinkedHashMap GetUserList();
}
