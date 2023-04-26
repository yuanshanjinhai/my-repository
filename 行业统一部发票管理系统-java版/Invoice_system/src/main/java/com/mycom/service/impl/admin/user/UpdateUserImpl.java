package com.mycom.service.impl.admin.user;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemUserEntity;
import com.mycom.general_tools.Md5Encrypt;
import com.mycom.mapper.SystemUserMapper;
import com.mycom.service.admin.user.UpdateUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class UpdateUserImpl extends ServiceImpl<SystemUserMapper, SystemUserEntity> implements UpdateUserService {
    @Autowired
    SystemUserMapper systemUserMapper;

    public LinkedHashMap UpdateUser(SystemUserEntity systemUserEntity){
        String userLoginName = systemUserEntity.getUser_login_name();
        String userName = systemUserEntity.getUser_name();
        String password = systemUserEntity.getPassword();
        Integer companyId = systemUserEntity.getCompany_id();
        Integer departmentId = systemUserEntity.getDepartment_id();

        String errorStr = "";

        if(userLoginName == null){
            errorStr += "登录名不能为空；";
        }
        if(userLoginName.length() >30){
            errorStr += "登录名不能超过30个字；";
        }
        QueryWrapper<SystemUserEntity> qw = new QueryWrapper<>();
        List<SystemUserEntity> rlist0 = systemUserMapper.selectList(qw);
        List userLoginNameList = new ArrayList();
        for(int i=0;i<rlist0.size();i++){
            if(rlist0.get(i).getUser_login_name().equals(userLoginName) != true){
                userLoginNameList.add(rlist0.get(i).getUser_login_name());
            }
        }

        if(userLoginNameList.contains(userLoginName) == true){
            errorStr += "登录名已存在；";
        }

        if(userName == null){
            errorStr += "用户名不能为空；";
        }
        if(userName.length() > 50){
            errorStr += "用户名不错超过50个字；";
        }

        if(password.length() < 6 || password.length()>16){
            errorStr += "密码必须在6-16位之间；";
        }

        if(companyId == null){
            errorStr += "公司id不能为空；";
        }

        if(departmentId == null){
            errorStr += "部门id不能为空；";
        }

        Map lmp = new LinkedHashMap();
        if(errorStr != ""){
            lmp.put("code",0);
            lmp.put("info","faid");
            lmp.put("data",errorStr);
        }
        else {
            Md5Encrypt ins = new Md5Encrypt();
            String md5Password = ins.getmd5(password);
            systemUserEntity.setPassword(md5Password);
            int r = systemUserMapper.updateById(systemUserEntity);
            if(r == 0){
                lmp.put("code",0);
                lmp.put("info","faid");
                lmp.put("data","更新失败；");
            }
            else {
                lmp.put("code",1);
                lmp.put("info","success");
            }
        }
        return (LinkedHashMap) lmp;
    }
}
