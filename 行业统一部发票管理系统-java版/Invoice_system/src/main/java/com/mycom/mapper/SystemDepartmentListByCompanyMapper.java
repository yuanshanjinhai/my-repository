package com.mycom.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.mycom.model.SystemDepartmentListByCompanyVO;
import org.apache.ibatis.annotations.Select;

import java.util.ArrayList;
import java.util.Map;

public interface SystemDepartmentListByCompanyMapper extends BaseMapper<SystemDepartmentListByCompanyVO> {
    @Select("<script>SELECT d.id,d.department_name " +
            "FROM system_department d,system_company_department cd " +
            "WHERE cd.company_id=#{companyId} AND cd.department_id=d.id</script>")
    ArrayList<Map> selectDepartmentList(Integer companyId);

    @Select("<script>SELECT d.department_name,d.department_explain " +
            "FROM system_department d,system_company_department cd " +
            "WHERE cd.company_id=#{companyId} AND cd.department_id=d.id</script>")
    ArrayList<Map> selectAllDepartmentByCompanyId(Integer companyId);
}
