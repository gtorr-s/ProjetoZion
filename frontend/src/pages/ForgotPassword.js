import React, { useState } from 'react';
import { Container, Row, Col, Form, Button, Card } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function ForgotPassword() {
    const [email, setEmail] = useState('');

    const handleForgotPassword = (event) => {
        event.preventDefault();
        // Adicione a lógica para enviar o email de recuperação de senha
        console.log('Email para recuperação:', email);
    };

    return (
        <Container fluid className="d-flex align-items-center justify-content-center min-vh-100" style={{ backgroundColor: '#f8f9fa' }}>
            <Row>
                <Col>
                    <Card className="p-4 shadow" style={{ width: '100%', maxWidth: '400px' }}>
                        <Card.Body>
                            <h3 className="text-center mb-4">Forgot Password</h3>
                            <Form onSubmit={handleForgotPassword}>
                                <Form.Group controlId="formEmail">
                                    <Form.Label>Email</Form.Label>
                                    <Form.Control
                                        type="email"
                                        placeholder="Enter your email to reset password"
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                        required
                                    />
                                </Form.Group>
                                <Button variant="primary" type="submit" className="w-100 mt-4">
                                    Send Reset Link
                                </Button>
                            </Form>
                            <div className="text-center mt-3">
                                <Link to="/" className="small">Back to Login</Link>
                            </div>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
}

export default ForgotPassword;
