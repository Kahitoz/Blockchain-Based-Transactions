import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Col, Form, Row } from "antd";
import { Log_in_user } from "../../Logic/LoginLogic";
const Login = () => {
  const [key, setKey] = useState("");
  const navigate = useNavigate();

  const handleKeyChange = (e) =>{
    setKey(e.target.value);
  }

  const HandleOnclickButtonChange = async(value)=>{
    await Log_in_user(value);
    
  }
  return (
    <div className="bg-gradient flex items-center justify-center h-screen">
      <div className="card w-400 p-2">
        <div className="flex items-center justify-between">
          <h1 className="text-2xl">KYŌMI - EXISTING USER</h1>
        </div>
        <hr />
        <Form layout="vertical">
          <Row gutter={16}>
            <Col span={24}>
              <Form.Item label="PRIVATE-KEY" name="PRIVATE-KEY">
                <input type="text" 
                value = {key}
                placeholder="Your Private Key"
                onChange={handleKeyChange}/>
              </Form.Item>
            </Col>
          </Row>

          <button className="primary-contained-btn w-100" type="submit" onClick={()=>HandleOnclickButtonChange(key)}>
            Login
          </button>
          <h1
            className="text-sm underline mt-2"
            onClick={() => navigate("/register")}
          >
            Not a member , Click Here To Register
          </h1>
        </Form>
      </div>
    </div>
  );
};

export default Login;
