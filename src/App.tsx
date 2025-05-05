import React, { useState } from 'react';

interface FormData {
  name: string;
  last_name: string;
  sex: 'male' | 'female';
  birth_date: string;
  weight_kg: number;
  height_cm: number;
  goal: 'lose fat' | 'gain weight' | 'maintain';
  restrictions: string;
  diet_type: 'Vegetarian' | 'Vegan' | 'Keto' | 'Paleo';
  fat_pref: 'Low' | 'Moderate' | 'High';
  protein_pref: 'Low' | 'Moderate' | 'High';
  carb_pref: 'Low' | 'Moderate' | 'High';
}

interface MacrosData {
  fat: string;
  protein: string;
  carbohydrates: string;
}

function App() {
  const [formData, setFormData] = useState<FormData>({
    name: '',
    last_name: '',
    sex: 'male',
    birth_date: '',
    weight_kg: 0,
    height_cm: 0,
    goal: 'maintain',
    restrictions: '',
    diet_type: 'Vegetarian',
    fat_pref: 'Moderate',
    protein_pref: 'Moderate',
    carb_pref: 'Moderate'
  });

  const [macros, setMacros] = useState<MacrosData | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch('YOUR_ENDPOINT_HERE', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error('Failed to submit form');

      const macrosResponse = await fetch('YOUR_MACROS_ENDPOINT');
      const macrosData = await macrosResponse.json();
      setMacros(macrosData);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl p-6">
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="grid grid-cols-1 gap-6">
            {/* Existing fields */}
            <inputField label="Name" name="name" value={formData.name} onChange={handleInputChange} />
            <inputField label="Last Name" name="last_name" value={formData.last_name} onChange={handleInputChange} />
            <selectField label="Sex" name="sex" options={['male', 'female']} value={formData.sex} onChange={handleInputChange} />
            <inputField type="date" label="Birth Date" name="birth_date" value={formData.birth_date} onChange={handleInputChange} />
            <inputField type="number" label="Weight (kg)" name="weight_kg" value={formData.weight_kg} onChange={handleInputChange} />
            <inputField type="number" label="Height (cm)" name="height_cm" value={formData.height_cm} onChange={handleInputChange} />
            <selectField label="Goal" name="goal" options={['lose fat', 'gain weight', 'maintain']} value={formData.goal} onChange={handleInputChange} />
            
            {/* New diet fields */}
            <selectField label="Diet Type" name="diet_type" options={['Vegetarian', 'Vegan', 'Keto', 'Paleo']} value={formData.diet_type} onChange={handleInputChange} />
            <selectField label="Fat Preference" name="fat_pref" options={['Low', 'Moderate', 'High']} value={formData.fat_pref} onChange={handleInputChange} />
            <selectField label="Protein Preference" name="protein_pref" options={['Low', 'Moderate', 'High']} value={formData.protein_pref} onChange={handleInputChange} />
            <selectField label="Carbohydrate Preference" name="carb_pref" options={['Low', 'Moderate', 'High']} value={formData.carb_pref} onChange={handleInputChange} />

            <div>
              <label htmlFor="restrictions" className="block text-sm font-medium text-gray-700">Dietary Restrictions</label>
              <textarea
                name="restrictions"
                id="restrictions"
                rows={3}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
                value={formData.restrictions}
                onChange={handleInputChange}
              />
            </div>
          </div>

          <div className="flex justify-end">
            <button
              type="submit"
              className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
            >
              Calculate Macros
            </button>
          </div>
        </form>

        {macros && (
          <div className="mt-6 p-4 bg-gray-50 rounded-lg">
            <h2 className="text-lg font-medium text-gray-900 mb-4">Your Recommended Macros</h2>
            <div className="space-y-2">
              <p className="text-sm text-gray-600">Fat: {macros.fat}</p>
              <p className="text-sm text-gray-600">Protein: {macros.protein}</p>
              <p className="text-sm text-gray-600">Carbohydrates: {macros.carbohydrates}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

// Reusable input field component
const inputField = ({ label, name, value, onChange, type = 'text' }: any) => (
  <div>
    <label htmlFor={name} className="block text-sm font-medium text-gray-700">{label}</label>
    <input
      type={type}
      name={name}
      id={name}
      required
      className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
      value={value}
      onChange={onChange}
    />
  </div>
);

// Reusable select field component
const selectField = ({ label, name, options, value, onChange }: any) => (
  <div>
    <label htmlFor={name} className="block text-sm font-medium text-gray-700">{label}</label>
    <select
      name={name}
      id={name}
      required
      className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm"
      value={value}
      onChange={onChange}
    >
      {options.map((opt: string) => (
        <option key={opt} value={opt}>{opt}</option>
      ))}
    </select>
  </div>
);

export default App;
