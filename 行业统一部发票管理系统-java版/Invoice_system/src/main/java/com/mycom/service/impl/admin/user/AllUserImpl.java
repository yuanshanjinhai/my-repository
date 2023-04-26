package com.mycom.service.impl.admin.user;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.entity.SystemCompanyEntity;
import com.mycom.entity.SystemDepartmentEntity;
import com.mycom.entity.SystemUserEntity;
import com.mycom.mapper.SystemCompanyMapper;
import com.mycom.mapper.SystemDepartmentMapper;
import com.mycom.mapper.SystemUserMapper;
import com.mycom.service.admin.user.AllUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class AllUserImpl extends ServiceImpl<SystemUserMapper, SystemUserEntity> implements AllUserService {
    @Autowired
    SystemUserMapper systemUserMapper;
    @Autowired
    SystemCompanyMapper systemCompanyMapper;
    @Autowired
    SystemDepartmentMapper systemDepartmentMapper;

    @Override
    public LinkedHashMap GetAllUser(Integer companyId,Integer departmentId){
        List<SystemUserEntity> rlist0 = null;
        if(companyId == null && departmentId == null){
            QueryWrapper<SystemUserEntity> qwUser = new QueryWrapper<>();
            rlist0 = systemUserMapper.selectList(qwUser);
        }
        if (companyId != null && departmentId == null){
            QueryWrapper<SystemUserEntity> qw = new QueryWrapper<>();
            qw.select().eq("company_id",companyId.toString());
            rlist0 = systemUserMapper.selectList(qw);
        }
        if(companyId == null && departmentId != null){
            QueryWrapper<SystemUserEntity> qw = new QueryWrapper<>();
            qw.select().eq("department_id",departmentId.toString());
            rlist0 = systemUserMapper.selectList(qw);
        }
        if(companyId != null && departmentId != null){
            QueryWrapper<SystemUserEntity> qw = new QueryWrapper<>();
            qw.select().eq("company_id",companyId.toString()).eq("department_id",departmentId.toString());
            rlist0 = systemUserMapper.selectList(qw);
        }
        List rlist = new ArrayList();
        for(int i =0;i<rlist0.size();i++){
            Map lmp0 = new LinkedHashMap();
            lmp0.put("id",rlist0.get(i).getId());
            lmp0.put("user_name",rlist0.get(i).getUser_name());

            Integer companyId1 = rlist0.get(i).getCompany_id();
            SystemCompanyEntity systemCompanyEntity = systemCompanyMapper.selectById(companyId1);
            String companyName = systemCompanyEntity.getCompany_name();
            lmp0.put("company_name",companyName);

            Integer departmentId1 = rlist0.get(i).getDepartment_id();
            SystemDepartmentEntity systemDepartmentEntity = systemDepartmentMapper.selectById(departmentId1);
            String departmentName = systemDepartmentEntity.getDepartment_name();
            lmp0.put("departmen_name",departmentName);

            rlist.add(lmp0);
        }
        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",rlist);
        return (LinkedHashMap) lmp;
    }
}
// http://127.0.0.1:5003/all_user
// http://127.0.0.1:5003/all_user?companyId=3
// http://127.0.0.1:5003/all_user?departmentId=2
// http://127.0.0.1:5003/all_user?companyId=3&departmentId=2