from OpenGL import GL

#aula 6
class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):
        #OpenGL version and requirements
        extension = "#extension GL_ARB_shading_language_420pack: require\n"
        shaderCode = "#version 130 \n " + extension + shaderCode

        shaderRef = GL.glCreateShader(shaderType)
        GL.glShaderSource(shaderRef, shaderCode)
        GL.glCompileShader(shaderRef)

        compileSuccess = GL.glGetShaderiv(shaderRef, GL.GL_COMPILE_STATUS)

        if not compileSuccess:
            errorMessage = GL.glGetShaderInfoLog(shaderRef)
            GL.glDeleteShader(shaderRef)
            errorMessage = "\n" + errorMessage.decode("utf-8")
            raise Exception( errorMessage )
        
        return shaderRef

    @staticmethod
    def initializeProgram( vertexShaderCode, fragmentShaderCode ):
        vertexShaderRef = OpenGLUtils.initializeShader(
            vertexShaderCode, GL.GL_VERTEX_SHADER)
        fragmentShaderRef = OpenGLUtils.initializeShader(
            fragmentShaderCode, GL.GL_FRAGMENT_SHADER)
        
        programRef = GL.glCreateProgram()

        GL.glAttachShader(programRef, vertexShaderRef)
        GL.glAttachShader(programRef, fragmentShaderRef)

        GL.glLinkProgram(programRef)

        linkSuccess = GL.glGetProgramiv( programRef, GL.GL_LINK_STATUS)

        if not linkSuccess:
            errorMessage = GL.glGetShaderInfoLog(programRef)
            GL.glDeleteShader(programRef)
            errorMessage = "\n" + errorMessage.decode("utf-8")
            raise Exception( errorMessage )

        return programRef
