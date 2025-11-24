// js/app.js

// 1. Captura de elementos del DOM (Document Object Model)
const formulario = document.getElementById('formulario-calculadora');
const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const operacionSelect = document.getElementById('operacion');
const resultadoArea = document.getElementById('resultado-area');

// Objeto para mapear las operaciones y saber si son unarias o binarias
// Esto ayuda en la validación del campo num2
const tipoOperacion = {
    'sumar': 'binaria',
    'restar': 'binaria',
    'multiplicar': 'binaria',
    'dividir': 'binaria',
    'potenciar': 'binaria',
    'logaritmo_base': 'binaria',
    'raiz_cuadrada': 'unaria' // Solo necesita num1
};

// 2. Event Listener para el formulario
formulario.addEventListener('submit', function(e) {
    e.preventDefault(); // Detener el envío clásico del formulario

    const operacion = operacionSelect.value;
    const num1 = parseFloat(num1Input.value);
    const num2 = parseFloat(num2Input.value);
    
    // Validaciones básicas de JS (Tipo de datos y existencia)
    if (isNaN(num1) || operacion === "") {
        mostrarResultado("Error: Debe ingresar al menos un número y seleccionar una operación.", 'alert-danger');
        return;
    }

    // 3. Validación de Campos Necesarios (Lógica de control)
    if (tipoOperacion[operacion] === 'binaria' && isNaN(num2)) {
        mostrarResultado("Error: Esta operación requiere un segundo número (b/exponente/base).", 'alert-warning');
        return;
    }

    // Si es unaria, nos aseguramos que el num2 sea null o 0 para la simulación
    const argumento2 = tipoOperacion[operacion] === 'unaria' ? null : num2;

    // 4. Simulación de Llamada a la API de Django (Usando fetch ES6)
    simularLlamadaAPI(operacion, num1, argumento2);
});

/**
 * Función que simula la comunicación con un endpoint REST de Django.
 * En un entorno real, aquí usarías la URL real de tu backend.
 * Por ejemplo: fetch('/api/calcular/', { method: 'POST', body: ... })
 * @param {string} operacion Nombre de la operación a realizar.
 * @param {number} a Primer argumento.
 * @param {number | null} b Segundo argumento.
 */
function simularLlamadaAPI(operacion, a, b) {
    
    // Construcción del objeto de datos a enviar al backend
    const datosEnvio = {
        operacion: operacion,
        num1: a,
        num2: b
    };

    mostrarResultado("Calculando... Enviando datos a Django (simulado)...", 'alert-secondary');

    // **Simulación de la Promesa (Asincronía ES6)**
    // Simulamos un retraso de red y una respuesta del servidor.
    new Promise(resolve => setTimeout(resolve, 800)) 
        .then(() => {
            // **Aquí se realizaría la lógica de cálculo real en el frontend para el ejemplo**
            // En Django, esta lógica estaría en las Vistas (Views) de Python.
            const resultadoSimulado = realizarCalculoLocal(operacion, a, b);

            // Simulación de respuesta exitosa de la API
            return { success: true, resultado: resultadoSimulado, mensaje: "Cálculo exitoso." };
        })
        .then(data => {
            if (data.success) {
                // Si el resultado es un string (Error de cálculo), lo manejamos como tal
                if (typeof data.resultado === 'string') {
                    mostrarResultado(`Operación fallida: ${data.resultado}`, 'alert-danger');
                } else {
                    mostrarResultado(`Resultado: ${data.resultado.toFixed(4)}`, 'alert-success');
                }
            } else {
                mostrarResultado(`Error de API: ${data.mensaje}`, 'alert-danger');
            }
        })
        .catch(() => {
            // Manejo de error de red o del servidor
            mostrarResultado("Error de conexión con el servidor (simulado).", 'alert-danger');
        });
}


/**
 * Función para demostrar la lógica de Python implementada ahora en JS para la simulación.
 * ESTA FUNCIÓN NO IRÍA EN EL PROYECTO REAL CON DJANGO.
 */
function realizarCalculoLocal(op, a, b) {
    switch (op) {
        case 'sumar': return a + b;
        case 'restar': return a - b;
        case 'multiplicar': return a * b;
        case 'dividir': 
            if (b === 0) return "División por cero.";
            return a / b;
        case 'potenciar': return Math.pow(a, b);
        case 'raiz_cuadrada': 
            if (a < 0) return "Raíz de negativo.";
            return Math.sqrt(a);
        case 'logaritmo_base':
            if (a <= 0 || b <= 0 || b === 1) return "Argumentos de logaritmo inválidos.";
            // Fórmula de cambio de base: log_b(a) = log(a) / log(b)
            return Math.log(a) / Math.log(b);
        default: return "Operación no reconocida.";
    }
}


/**
 * Muestra el resultado en el área designada y cambia la clase de alerta.
 */
function mostrarResultado(mensaje, clase) {
    resultadoArea.className = `alert mt-4 ${clase}`;
    resultadoArea.textContent = mensaje;
}

// Llama a una función de inicialización si es necesario
// console.log("Calculadora JS inicializada.");