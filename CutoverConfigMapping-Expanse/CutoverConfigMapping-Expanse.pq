// This file contains your Data Connector logic
[Version = "1.0.0"]
section CutoverConfigMapping-Expanse;

[DataSource.Kind="CutoverConfigMapping-Expanse", Publish="CutoverConfigMapping-Expanse.Publish"]
shared CutoverConfigMapping-Expanse.Contents = (optional message as text) =>
    let
        _message = if (message <> null) then message else "(no message)",
        a = "Hello from CutoverConfigMapping-Expanse: " & _message
    in
        a;

// Data Source Kind description
CutoverConfigMapping-Expanse = [
    Authentication = [
        // Key = [],
        // UsernamePassword = [],
        // Windows = [],
        Anonymous = []
    ]
];

// Data Source UI publishing description
CutoverConfigMapping-Expanse.Publish = [
    Beta = true,
    Category = "Other",
    ButtonText = { Extension.LoadString("ButtonTitle"), Extension.LoadString("ButtonHelp") },
    LearnMoreUrl = "https://powerbi.microsoft.com/",
    SourceImage = CutoverConfigMapping-Expanse.Icons,
    SourceTypeImage = CutoverConfigMapping-Expanse.Icons
];

CutoverConfigMapping-Expanse.Icons = [
    Icon16 = { Extension.Contents("CutoverConfigMapping-Expanse16.png"), Extension.Contents("CutoverConfigMapping-Expanse20.png"), Extension.Contents("CutoverConfigMapping-Expanse24.png"), Extension.Contents("CutoverConfigMapping-Expanse32.png") },
    Icon32 = { Extension.Contents("CutoverConfigMapping-Expanse32.png"), Extension.Contents("CutoverConfigMapping-Expanse40.png"), Extension.Contents("CutoverConfigMapping-Expanse48.png"), Extension.Contents("CutoverConfigMapping-Expanse64.png") }
];
