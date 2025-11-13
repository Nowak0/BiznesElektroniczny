<?php

namespace Symfony\Config\UxIcons;

use Symfony\Component\Config\Loader\ParamConfigurator;
use Symfony\Component\Config\Definition\Exception\InvalidConfigurationException;

/**
 * This class is automatically generated to help in creating a config.
 */
class IconSetsConfig 
{
    private $path;
    private $alias;
    private $iconAttributes;
    private $_usedProperties = [];

    /**
     * The local icon set directory path.
     * (cannot be used with 'alias')
     * @example %kernel.project_dir%/assets/svg/acme
     * @default null
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function path($value): static
    {
        $this->_usedProperties['path'] = true;
        $this->path = $value;

        return $this;
    }

    /**
     * The remote icon set identifier.
     * (cannot be used with 'path')
     * @example simple-icons
     * @default null
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function alias($value): static
    {
        $this->_usedProperties['alias'] = true;
        $this->alias = $value;

        return $this;
    }

    /**
     * @param ParamConfigurator|list<ParamConfigurator|mixed> $value
     *
     * @return $this
     */
    public function iconAttributes(ParamConfigurator|array $value): static
    {
        $this->_usedProperties['iconAttributes'] = true;
        $this->iconAttributes = $value;

        return $this;
    }

    public function __construct(array $value = [])
    {
        if (array_key_exists('path', $value)) {
            $this->_usedProperties['path'] = true;
            $this->path = $value['path'];
            unset($value['path']);
        }

        if (array_key_exists('alias', $value)) {
            $this->_usedProperties['alias'] = true;
            $this->alias = $value['alias'];
            unset($value['alias']);
        }

        if (array_key_exists('icon_attributes', $value)) {
            $this->_usedProperties['iconAttributes'] = true;
            $this->iconAttributes = $value['icon_attributes'];
            unset($value['icon_attributes']);
        }

        if ([] !== $value) {
            throw new InvalidConfigurationException(sprintf('The following keys are not supported by "%s": ', __CLASS__).implode(', ', array_keys($value)));
        }
    }

    public function toArray(): array
    {
        $output = [];
        if (isset($this->_usedProperties['path'])) {
            $output['path'] = $this->path;
        }
        if (isset($this->_usedProperties['alias'])) {
            $output['alias'] = $this->alias;
        }
        if (isset($this->_usedProperties['iconAttributes'])) {
            $output['icon_attributes'] = $this->iconAttributes;
        }

        return $output;
    }

}
