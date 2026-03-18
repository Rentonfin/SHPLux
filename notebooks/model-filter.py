import numpy as np
class Filter:
# Determening nearest neighbours for stars
    def __init__(
    self,
    label_data,
    tolerances: bool):
        self.labels_full = label_data_h["labels"]
        self.names = label_data_h["label_names"]
        self.labels_err_full = label_data_h["labels_err"]
        self.err_names = label_data_h["label_names_err"]
        self.k_same = 1
        self.k_diff = 3.0
        self.tol_teff = 20
        self.tol_logg = 0.1
        self.tol_abundancy = 0.076

        test_ind = 4000
        labels = np.array(labels_full[test_ind:]) 
        labels_err = np.array(labels_err_full[test_ind:])


        # --- values ---
        i_teff = names.index("teff")
        teff = labels[:, i_teff]
        i_logg = names.index("logg")
        logg = labels[:, i_logg]
        i_fe_h = names.index("fe_h")
        Fe_h = labels[:, i_fe_h]

        i_Li_h = names.index("Li_h")
        Li_h = labels[:, i_Li_h]
        i_Na_h = names.index("Na_h")
        Na_h = labels[:, i_Na_h]
        i_O_h  = names.index("O_h")
        O_h  = labels[:, i_O_h]
        i_Mg_h = names.index("Mg_h")
        Mg_h = labels[:, i_Mg_h]
        i_Y_h  = names.index("Y_h")
        Y_h  = labels[:, i_Y_h]
        i_Ce_h = names.index("Ce_h")
        Ce_h = labels[:, i_Ce_h]
        i_Ba_h = names.index("Ba_h")
        Ba_h = labels[:, i_Ba_h]
        i_Eu_h = names.index("Eu_h")
        Eu_h = labels[:, i_Eu_h]

        # --- errors ---
        i_e_teff = err_names.index("e_teff")
        teff_errors = labels_err[:, i_e_teff]
        i_e_logg = err_names.index("e_logg")
        logg_errors = labels_err[:, i_e_logg]
        i_e_fe_h = err_names.index("e_fe_h")
        fe_h_errors = labels_err[:, i_e_fe_h]

        i_e_Li_h = err_names.index("e_Li_h")
        Li_h_errors = labels_err[:, i_e_Li_h]
        i_e_Na_h = err_names.index("e_Na_h")
        Na_h_errors = labels_err[:, i_e_Na_h]
        i_e_O_h  = err_names.index("e_O_h")
        O_h_errors  = labels_err[:, i_e_O_h]
        i_e_Mg_h = err_names.index("e_Mg_h")
        Mg_h_errors = labels_err[:, i_e_Mg_h]
        i_e_Y_h  = err_names.index("e_Y_h")
        Y_h_errors  = labels_err[:, i_e_Y_h]
        i_e_Ce_h = err_names.index("e_Ce_h")
        Ce_h_errors = labels_err[:, i_e_Ce_h]
        i_e_Ba_h = err_names.index("e_Ba_h")
        Ba_h_errors = labels_err[:, i_e_Ba_h]
        i_e_Eu_h = err_names.index("e_Eu_h")
        Eu_h_errors = labels_err[:, i_e_Eu_h]

    def error_satistical_model(k, error_reference, errors):
        errors = np.maximum(errors, 1e-12)
        error_reference = np.maximum(error_reference, 1e-12)
        tol = k* np.sqrt(error_reference**2 + errors**2)
        return tol

    k_same = 1
    k_diff = 3.0
    tol_teff = 20
    tol_logg = 0.1
    tol_abundancy = 0.076
    pairs = [] 

    """I've done this in two different ways. one sets arbritrary tollerance values, one says if the diference is less than the standard error on the difference to within 1 sigma then they are the same 
    """
    if self.tolerances:

        for i in range(len(teff)):
            match = (np.abs(teff - teff[i]) <= tol_teff) \
                & (np.abs(logg - logg[i]) <= tol_logg) \
                & (np.abs(fe_h  - Fe_h[i])  <= tol_abundancy) \
                & (np.abs(Mg_h - Mg_h[i]) <= tol_abundancy) \
                & (np.abs(Li_h  - Li_h[i])  <= tol_abundancy) \
                & (np.abs(Na_h  - Na_h[i])  <= tol_abundancy) \
                & (np.abs(O_h  - O_h[i])  <= tol_abundancy) \
                & (np.abs(Y_h  - Y_h[i])  <= tol_abundancy) \
                & (np.abs(Ce_h  - Ce_h[i])  <= tol_abundancy) \
                & (np.abs(Ba_h  - Ba_h[i])  <= tol_abundancy) \
                & (np.abs(Eu_h  - Eu_h[i])  >= diff_abundancy) \
            
    # for i in range(len(teff)):
    #     match = (
    #         (np.abs(teff - teff[i]) <= error_satistical_model(k_same, teff_errors[i], teff_errors)) &
    #         (np.abs(logg - logg[i]) <= error_satistical_model(k_same, logg_errors[i], logg_errors)) &
    #         (np.abs(Fe_h - Fe_h[i]) <= error_satistical_model(k_same, fe_h_errors[i], fe_h_errors)) &
    #         (np.abs(Mg_h - Mg_h[i]) <= error_satistical_model(k_same, Mg_h_errors[i], Mg_h_errors)) &
    #         # Li must be DIFFERENT (k_diff sigma away)
    #         (np.abs(Li_h - Li_h[i]) >= error_satistical_model(k_diff, Li_h_errors[i], Li_h_errors)) &
    #         (np.abs(Na_h - Na_h[i]) <= error_satistical_model(k_same, Na_h_errors[i], Na_h_errors)) &
    #         (np.abs(O_h  - O_h[i])  <= error_satistical_model(k_same, O_h_errors[i],  O_h_errors))  &
    #         (np.abs(Y_h  - Y_h[i])  <= error_satistical_model(k_same, Y_h_errors[i],  Y_h_errors))  &
    #         (np.abs(Ce_h - Ce_h[i]) <= error_satistical_model(k_same, Ce_h_errors[i], Ce_h_errors)) &
    #         (np.abs(Ba_h - Ba_h[i]) <= error_satistical_model(k_same, Ba_h_errors[i], Ba_h_errors)) &
    #         (np.abs(Eu_h - Eu_h[i]) <= error_satistical_model(k_same, Eu_h_errors[i], Eu_h_errors))
    #   )
        
        match[i] = False  # exclude itself
        js = np.where(match)[0] #where returns a tupple, this looks like [[True, False, False, True, False]], returns indices where True, i.e the above condition is met

        for j in js:
            if i < j: #exlude smaller as double count
                pairs.append((i, j))

    print(pairs)


    print(labels[(pairs)])

    i,j = pairs[0]
    spec_i = spectra_test_fromflux[i]
    spec_j = spectra_test_fromflux[j]
    wavelengths = spectra_data["wl"]

    diff_spectra = spec_i - spec_j

