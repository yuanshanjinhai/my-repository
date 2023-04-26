package com.mycom.service.impl.alllist;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemUserEntity;
import com.mycom.mapper.SystemUserMapper;
import com.mycom.service.alllist.ListUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class ListUserServiceImpl extends ServiceImpl<SystemUserMapper, SystemUserEntity> implements ListUserService {
    @Autowired
    SystemUserMapper systemUserMapper;

    @Override
    public LinkedHashMap GetUserList(){
        QueryWrapper<SystemUserEntity> qw = new QueryWrapper<>();
        List<SystemUserEntity> rlist0 = systemUserMapper.selectList(qw);
        List rlist = new ArrayList();
        for(int i =0;i<rlist0.size();i++){
            Map lmp0 = new LinkedHashMap();
            lmp0.put("id",rlist0.get(i).getId());
            lmp0.put("user_name",rlist0.get(i).getUser_name());
            rlist.add(lmp0);
        }
        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",rlist);
        return (LinkedHashMap) lmp;
    }
}
