import React, { createContext, useCallback, useState, useContext } from 'react';
import api from '../services/api';

interface AuthState {
  token: string;
  user: object;

}

interface SignInCredentials {
  username: string;
  password: string;
}

interface AuthContextStateData {
  user: object;
  signIn(credentials: SignInCredentials): Promise<void>;
  signOut(): void;
}

  const AuthContext = createContext<AuthContextStateData>({} as AuthContextStateData);

  const AuthProvider: React.FC = ({ children }) => {
    const [data, setData] = useState<AuthState>(() => {
      const token = localStorage.getItem('@MakeItEasy:token');
      const user = localStorage.getItem('@MakeItEasy:user');

      if (token && user ) {
        return { token, user: JSON.parse(user) }
      }

      return {} as AuthState;
    });

  const signIn = useCallback(async ({ username, password }) => {
    const response = await api.post('api-token-auth/', {
      username,
      password,
    });

    const { token, user } = response.data;

    localStorage.setItem('@MakeItEasy:token', token);
    localStorage.setItem('@MakeItEasy:user', JSON.stringify(user));

    setData({ token, user })

  }, []);

  const signOut = useCallback(() =>{
    localStorage.removeItem('@MakeItEasy:token');
    localStorage.removeItem('@MakeItEasy:user');

    setData({} as AuthState);


  }, []);

  return (
    <AuthContext.Provider value={{ user: data.user, signIn, signOut }}>
      {children}
    </AuthContext.Provider>
  );

};

function useAuth(): AuthContextStateData {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error(' useAuth must be used within an AuthProvider');
  }

  return context
}


export {AuthProvider, useAuth}



