
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('nutritionForm');
    const macrosResult = document.getElementById('macrosResult');
    const fatValue = document.getElementById('fatValue');
    const proteinValue = document.getElementById('proteinValue');
    const carbsValue = document.getElementById('carbsValue');

    let formDataStore = [];

    const mockMacros = {
        fat: "70-75%",
        protein: "20-25%",
        carbohydrates: "5-10%"
    };

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = {
            name: form.name.value,
            last_name: form.last_name.value,
            sex: form.sex.value,
            birth_date: form.birth_date.value,
            weight_kg: parseFloat(form.weight_kg.value),
            height_cm: parseFloat(form.height_cm.value),
            goal: form.goal.value,
            restrictions: form.restrictions.value,
            dietType: form.dietType.value,
            fat: form.fat.value,
            protein: form.protein.value,
            carbohydrates: form.carbohydrates.value
        };

        try {
            formDataStore.push(formData);
            console.log('Stored form data:', formDataStore);

            const arriaData = JSON.stringify(formData, null, 2);
            console.log('Data formatted for Arria Studio:', arriaData);

            await new Promise(resolve => setTimeout(resolve, 500));

            fatValue.textContent = mockMacros.fat;
            proteinValue.textContent = mockMacros.protein;
            carbsValue.textContent = mockMacros.carbohydrates;
            macrosResult.classList.remove('hidden');

        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while processing the form data. Please try again.');
        }
    });

    document.querySelector('.btn-new').addEventListener('click', () => {
        form.reset();
        macrosResult.classList.add('hidden');
    });

    document.querySelector('.btn-history').addEventListener('click', () => {
        console.log('All stored form submissions:', formDataStore);
    });
});
