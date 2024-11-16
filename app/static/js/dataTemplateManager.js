class DataTemplateManager  {
    constructor(jsonFilename) {
        this.jsonFilename = jsonFilename;
        this._template = null;
    }

    async _loadJsonTemplate() {
        const response = await fetch(`../json/${this.jsonFilename}`);
        
        if (!response.ok) {
            throw new Error(`JSON file ${this.jsonFilename} not found.`);
        }
        
        this._template = await response.json();
    }

    async initialize() {
        await this._loadJsonTemplate();
    }

    setValue(key, value) {
        if (this._template && key in this._template) {
            this._template[key] = value;
        } else {
            throw new Error(`Key ${key} not found in template ${this.jsonFilename}.`);
        }
    }

    getValue(key) {
        if (this._template && key in this._template) {
            return this._template[key];
        } else {
            throw new Error(`Key ${key} not found in template ${this.jsonFilename}.`);
        }
    }

    toJson() {
        return JSON.stringify(this._template);
    }

    fromJson(jsonString) {
        try {
            const data = JSON.parse(jsonString);
            for (const key in data) {
                if (key in this._template) {
                    this._template[key] = data[key];
                } else {
                    throw new Error(`Key ${key} not found in template ${this.jsonFilename}.`);
                }
            }
        } catch (error) {
            throw new Error("Invalid JSON string provided.");
        }
    }
}
