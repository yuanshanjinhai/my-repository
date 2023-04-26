package com.mycom.service.impl.admin.user;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemCompanyEntity;
import com.mycom.entity.SystemDepartmentEntity;
import com.mycom.entity.SystemUserEntity;
import com.mycom.mapper.SystemCompanyMapper;
import com.mycom.mapper.SystemDepartmentMapper;
import com.mycom.mapper.SystemUserMapper;
import com.mycom.service.admin.user.OneUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.LinkedHashMap;
import java.util.Map;

@Service
public class OneUserImpl extends ServiceImpl<SystemUserMapper, SystemUserEntity> implements OneUserService {
    @Autowired
    SystemUserMapper systemUserMapper;
    @Autowired
    SystemCompanyMapper systemCompanyMapper;
    @Autowired
    SystemDepartmentMapper systemDepartmentMapper;

    public LinkedHashMap OneUser(Integer userId){
        Map lmp = new LinkedHashMap();
        SystemUserEntity systemUserEntityOne = systemUserMapper.selectById(userId);
        if(systemUserEntityOne == null){
            lmp.put("code",0);
            lmp.put("info","faid");
            lmp.put("data","查询失败");
        }
        else {
            Map lmp0 = new LinkedHashMap();
            lmp0.put("user_login_name",systemUserEntityOne.getUser_login_name());
            lmp0.put("user_name",systemUserEntityOne.getUser_name());

            Integer companyId = systemUserEntityOne.getCompany_id();
            SystemCompanyEntity systemCompanyEntity = systemCompanyMapper.selectById(companyId);
            String companyName = systemCompanyEntity.getCompany_name();
            lmp0.put("company_id",companyName);

            Integer departmentId = systemUserEntityOne.getDepartment_id();
            SystemDepartmentEntity systemDepartmentEntityOne = systemDepartmentMapper.selectById(departmentId);
            String departmentName = systemDepartmentEntityOne.getDepartment_name();
            lmp0.put("department_id",departmentName);

            lmp.put("code",1);
            lmp.put("info","success");
            lmp.put("data",lmp0);
        }
        return (LinkedHashMap) lmp;
    }
}
